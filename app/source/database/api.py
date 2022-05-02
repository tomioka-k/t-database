from ninja import Router
from .apis import videos

router = Router(tags=['database'])
router.add_router("/video/",videos.router, tags=['Videos'])
