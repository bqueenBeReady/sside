from django.db import models
from django.db.models import permalink
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext, ugettext_lazy as _

@python_2_unicode_compatible
def getInfo(request):
    if(request.method == 'POST'):
        data = request.FILES.get('data')
        path = default_storage.save('coolio.wav',ContentFile(data.read()))
        tmpfile = os.path.join(settings.MEDIA_ROOT, path)
        pprint(tmpfile)
        # wav.write('myfile.wav',8000, data)
    return HttpResponse('cool')