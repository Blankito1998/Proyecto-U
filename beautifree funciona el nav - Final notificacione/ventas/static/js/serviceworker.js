
var staticCacheName = 'djangopwa-v1';
var cached_urls = [
  '/',
  '/ventas/Contactenos.html',
  '/ventas/QuienesSomos.html',
  '/ventas/Mision&Vision.html',
  '/ventas/index.html',
  '/ventas/listar_productos.html'
];
self.addEventListener('install', function (event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function (cache) {
      return cache.addAll(cached_urls);
    })
  );
});

self.addEventListener('fetch', function (event) {
  var requestUrl = new URL(event.request.url);
  if (requestUrl.origin === location.origin) {
    if ((requestUrl.pathname === '/')) {
      event.respondWith(caches.match(cached_urls));
      return;
    }
  }
  event.respondWith(
    caches.match(event.request).then(function (response) {      
      return response || fetch(event.request);
    })
  );
});

