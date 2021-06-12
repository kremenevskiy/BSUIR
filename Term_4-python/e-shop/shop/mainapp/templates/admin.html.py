# import extends as extends
#
# {% extends 'admin/change_form.html' %}
# {% load static %}
#
# {% block admin_change_form_document_ready %}
# {{ block.super }}
# <script>
#
# (function($) {
#     $('#sd').on('click', function(){
#         if($('#sd').prop('checked') == true){
#             $('#sd_type').prop('readonly', false)
#             $('#sd_type').val('')
#             $('#sd_type').css('background', 'white')
#         }else{
#             $('#sd_type').prop('readonly', true)
#             $('#sd_type').val('')
#             $('#sd_type').css('background', 'lightgrey')
#         }
#     })
# })(django.jQuery);
# </script>
# {% endblock %}