def search(request):
    if request.GET.has_key("q"):
         
        return ({"searched_term" : request.GET['q']})
    else:
        return {}