from django.utils.translation import ugettext_lazy as _


QUESTION_TYPE_CHOICES = (
    (1, _("text")),
    (2, _("textarea")),
    (3, _("Maybe relevant")),
    (4, _("Relevant")),
    (5, _("Leading candidate"))
)
