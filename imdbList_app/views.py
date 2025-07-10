# from django.shortcuts import render
# from imdbList_app.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     print(movies.values())
#     data = {
#         "movies": list(movies.values())  # Converting QuerySet to list of dictionaries for JSON serialization
#     }
#     return JsonResponse(data)

# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     # print(movie)
#     data = {
#         'name' : movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     return JsonResponse(data)
    

