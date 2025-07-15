from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
 
 
 
class WatchListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'records'  #Page name in URL
    page_size_query_param = 'p_size' #override the page size request from client side
    max_page_size = 10
    # last_page_strings = 'end'    #override the last page name as end
    
    
class WatchListLOPagination(LimitOffsetPagination): #used for sharing our API to access limited resources at one page
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
    
class WatchListCPagination(CursorPagination): # cannot change the exact page number
    page_size = 10
    ordering = 'created'
    cursor_query_param = 'record'
    
    


    