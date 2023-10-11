# myapp/templatetags/footer_tags.py

from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('footer.html')
def render_footer(company_name="My Company"):
    current_year = datetime.now().year
    return {'current_year': current_year, 'company_name': company_name}
