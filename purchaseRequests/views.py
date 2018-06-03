from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Request


def list(request):
    pur_req_list = Request.objects.all().order_by('-timestamp')
    return render(request, "purchaseRequests/list.html", {'pur_req_list': pur_req_list})

def new(request):
    return render(request, "purchaseRequests/new_request.html")

def detail(request, pReq_id):
    pur_req = get_object_or_404(Request, pk=pReq_id)
    unappr = ""
    undec = ""
    appr = ""
    if pur_req.approved is True:
        appr = "selected-appr"
    elif pur_req.approved is False:
        unappr = "selected-unappr"
    else:
        undec = "selected-undec"

    return render(request, "purchaseRequests/detail.html", {'pur_req': pur_req,
                                                            'unappr_class': unappr,
                                                            'undec_class': undec,
                                                            'appr_class': appr,})

def edit(request, pReq_id):
    pur_req = get_object_or_404(Request, pk=pReq_id)
    return render(request, "purchaseRequests/edit.html")

