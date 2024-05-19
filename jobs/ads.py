from django.http import HttpResponse
from django.views import View

class AdsTxtView(View):
  """A view that serves the ads.txt content"""
  def get(self, request, *args, **kwargs):
    # Replace 'your_publisher_id' with your actual Google Adsense publisher ID
    content = "google.com, pub-6541033542795675, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")
