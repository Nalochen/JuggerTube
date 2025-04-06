from flask import request

from config.cache import cache


def create_video_cache_key() -> str:
    """Create cache key for video"""

    videoId = request.view_args.get('videoId')

    return f"video-{videoId}"


def clearVideoCache(videoId: int) -> None:
    """Clear cache for video"""

    cache.delete('video-overview')

    cache.delete(f'video-{videoId}')


def clearCompleteVideoCache() -> None:
    """Clear complete video cache"""

    videoKeys = cache.cache._read_client.keys('video-*')

    [cache.delete(key.decode('utf-8')) for key in videoKeys]
