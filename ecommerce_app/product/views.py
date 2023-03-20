from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import ProductUploadImag
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.views import generic
from django.utils import timezone

# Create your views here.

def product_create_view(request):
    pass

def product_update_view(request, pk):
    pass

def product_detail_view(request, pk):
    pass

def product_delete_view(request, pk):
    pass

def product_category_list_view(request, pk, category):
    pass

def product_category_detail_view(request, pk, category, pk):
    pass

@login_required
def product_upload_view(request):
    if request.method == 'POST':
        product_file_name = request.FILES.get('file').name
        product_file = request.FILES.get('file')
        obj, created = ProductUploadImag.objects.get_or_create(file_name=product_file_name)

        if created:
            obj.product_file = product_file
            obj.save()
            with open(obj.product_file.path, 'r') as f:
                reader = uploadService.read(f)
                return HttpResponse(data=reader, content_type='image/jpeg')
        else:
            return JsonResponse({'ex': 'Error'})
    else:
        return HttpResponse()

@login_required
def create_product_data(request):
    form = ProductCreateForm(request.POST or None)
    if request.is_fetch():
        image = request.POST.get('image')
        img = get_product_image(image)
        account = Accout.objects.get(user=request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.image = image
            instance.account = account
            instance.save()
        return JsonResponse({'msg': 'send'})
    return JsonResponse({})

@login_required
def render_data_view(request, pk):
    template_path = 'productCreateForm/data.html'
    obj = get_object_404(ProductUploadImag, pk=pk)
    context = {'obj': obj}
    response = HttpResponse(content_type='image/jpeg')
    response['Content-Disposition'] = 'filename="image_file.jpeg"'
    template = get_template(template_path)
    html = template.render(context)

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'product_data_list'

    def get_queryset(self):
        return  Product.objects.filter(
            created__lte=timezone.now()
        )
        order_by('-created')[:5]


class DetailView(generic.DetailView):
    def get_queryset(self):
        return Product.objects.filter(created=timezone.now())


