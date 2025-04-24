# review/management/commands/export_reviews.py

import csv

from django.core.management.base import BaseCommand

from review.models import (
    ReviewAssignment,
    ReviewAssignmentAnswer,
    ReviewFormElement,
)


class Command(BaseCommand):
    help = "Export ReviewAssignments and their answers to CSV."

    def add_arguments(self, parser):
        parser.add_argument(
            "--journal",
            type=str,
            required=True,
            help="Journal code to filter ReviewAssignments by",
        )

    def handle(self, *args, **options):
        journal_code = options["journal"]
        filename = f"review_assignments_export_{journal_code}.csv"

        assignments = ReviewAssignment.objects.filter(
            article__journal__code=journal_code,
        ).select_related(
            "article",
            "reviewer",
            "editor",
        )

        if not assignments.exists():
            self.stdout.write(self.style.WARNING(f"No review assignments found for journal '{journal_code}'"))
            return

        all_elements = ReviewFormElement.objects.filter(
            id__in=ReviewAssignmentAnswer.objects.filter(
                assignment__in=assignments,
            ).values_list(
                "original_element_id",
                flat=True,
            ).distinct()
        )

        element_headers = {
            element.id: element.name or f"element_{element.id}"
            for element in all_elements
        }

        fieldnames = [
            "assignment_id",
            "article_id",
            "reviewer",
            "editor",
            "decision",
            "date_requested",
            "date_due",
            "date_accepted",
            "date_declined",
            "date_complete",
            "is_complete",
        ] + list(element_headers.values())

        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for assignment in assignments:
                row = {
                    "assignment_id": assignment.id,
                    "article_id": assignment.article_id,
                    "reviewer": assignment.reviewer.full_name(),
                    "editor": assignment.editor.full_name() if assignment.editor else '',
                    "decision": assignment.decision,
                    "date_requested": assignment.date_requested,
                    "date_due": assignment.date_due,
                    "date_accepted": assignment.date_accepted,
                    "date_declined": assignment.date_declined,
                    "date_complete": assignment.date_complete,
                    "is_complete": assignment.is_complete,
                }

                answers = ReviewAssignmentAnswer.objects.filter(
                    assignment=assignment
                )

                for answer in answers:
                    header = element_headers.get(answer.original_element_id)
                    if header:
                        row[header] = answer.edited_answer or answer.answer

                writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f"Exported data to {filename}"))
