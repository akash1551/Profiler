from django.conf.urls import patterns,include,url

urlpatterns = patterns('',
                       url(r'^add_data_page/','details.views.add_data_page'),
                       url(r'^save_data/','details.views.save_data'),
                       url(r'^save_json_data/','details.views.save_json_data'),
                       url(r'^get_data_from_db/','details.views.get_data_from_db'),
                       url(r'^send_file_to_json/','details.views.send_file_to_json'),

                       #url(r'^json_data/','books.views.book_date'),
                      
                      )