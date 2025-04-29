import io
import os
import traceback

from django.contrib import messages
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required

from submission.models import Article
from journal.models import Issue
from plugins.scripts.forms import TransformForm


XSLT_FILE_PATH = os.path.join(
    settings.BASE_DIR,
    "plugins",
    "scripts",
    "xsl",
    "abstracts.xsl",
)

TITLE_XSLT_FILE_PATH = os.path.join(
    settings.BASE_DIR,
    "plugins",
    "scripts",
    "xsl",
    "titles.xsl",
)


@staff_member_required
def scripts_manager(request):
    template = 'manager.html'
    context = {}
    return render(request, template, context)


@staff_member_required
def transform_abstract_view(
    request,
):
    """
    View to trigger the abstract transformation command.
    """
    if request.method == "POST":
        form = TransformForm(request.POST)

        if form.is_valid():
            article_id = form.cleaned_data.get("article_id")
            issue_id = form.cleaned_data.get("issue_id")

            options = {
                "xslt_file": XSLT_FILE_PATH,
            }

            if article_id:
                try:
                    article = Article.objects.get(
                        pk=article_id,
                        journal=request.journal,
                    )
                    options["article_id"] = article.pk
                except Article.DoesNotExist:
                    messages.error(
                        request,
                        f"Article ID {article_id} does not exist for this journal.",
                    )
                    return HttpResponseRedirect(request.path)

            elif issue_id:
                try:
                    issue = Issue.objects.get(
                        pk=issue_id,
                        journal=request.journal,
                    )
                    options["issue_ids"] = [issue.pk]
                except Issue.DoesNotExist:
                    messages.error(
                        request,
                        f"Issue ID {issue_id} does not exist for this journal.",
                    )
                    return HttpResponseRedirect(request.path)

            else:
                options["journal_codes"] = [request.journal.code]

            try:
                stdout = io.StringIO()
                call_command(
                    "jats_abstract_to_html",
                    stdout=stdout,
                    stderr=stdout,
                    **options,
                )
                messages.success(request, f"Transformation complete.\n{stdout.getvalue()}")
            except Exception as e:
                messages.error(
                    request,
                    f"An error occurred: {str(e)}\n{traceback.format_exc()}",
                )

            return HttpResponseRedirect(request.path)

    else:
        form = TransformForm()

    template = "transform_abstract_form.html"
    context = {
        "form": form,
    }
    return render(
        request,
        template,
        context,
    )


@staff_member_required
def transform_title_view(
    request,
):
    """
    View to trigger the title transformation command.
    """
    if request.method == "POST":
        form = TransformForm(request.POST)

        if form.is_valid():
            article_id = form.cleaned_data.get("article_id")
            issue_id = form.cleaned_data.get("issue_id")

            options = {
                "xslt_file": TITLE_XSLT_FILE_PATH,
            }

            if article_id:
                try:
                    article = Article.objects.get(
                        pk=article_id,
                        journal=request.journal,
                    )
                    options["article_id"] = article.pk
                except Article.DoesNotExist:
                    messages.error(
                        request,
                        f"Article ID {article_id} does not exist for this journal.",
                    )
                    return HttpResponseRedirect(request.path)

            elif issue_id:
                try:
                    issue = Issue.objects.get(
                        pk=issue_id,
                        journal=request.journal,
                    )
                    options["issue_ids"] = [issue.pk]
                except Issue.DoesNotExist:
                    messages.error(
                        request,
                        f"Issue ID {issue_id} does not exist for this journal.",
                    )
                    return HttpResponseRedirect(request.path)

            else:
                options["journal_codes"] = [request.journal.code]

            try:
                stdout = io.StringIO()
                call_command(
                    "jats_title_to_html",
                    stdout=stdout,
                    stderr=stdout,
                    **options,
                )
                messages.success(request, f"Transformation complete.\n{stdout.getvalue()}")
            except Exception as e:
                messages.error(
                    request,
                    f"An error occurred: {str(e)}\n{traceback.format_exc()}",
                )

            return HttpResponseRedirect(request.path)

    else:
        form = TransformForm()

    return render(
        request,
        "transform_title_form.html",
        {
            "form": form,
        },
    )