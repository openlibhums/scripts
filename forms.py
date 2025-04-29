from django import forms


class TransformForm(forms.Form):
    article_id = forms.IntegerField(
        required=False,
        label="Article ID",
    )
    issue_id = forms.IntegerField(
        required=False,
        label="Issue ID",
    )

    def clean(self):
        cleaned_data = super().clean()
        article_id = cleaned_data.get("article_id")
        issue_id = cleaned_data.get("issue_id")

        if not article_id and not issue_id:
            # No IDs provided — allowed, but confirm no conflict
            pass
        elif article_id and issue_id:
            raise forms.ValidationError(
                "Please provide either an Article ID or an Issue ID, not both."
            )

        return cleaned_data
