from django.views.generic.detail import SingleObjectMixin

# class CategoryDetailMixin(SingleObjectMixin):
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Category.objects.get_categories_for_left_sidebar()
#         return context