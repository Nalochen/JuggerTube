from flask import request
from DataDomain.Database.Repository import VideoRepository
from DataDomain.Model import Response


class GetPaginatedVideosHandler:
    """Handler for getting paginated videos"""

    @staticmethod
    def handle() -> Response:

        url = '/api/video-frontend/get-paginated-videos'

        videos = VideoRepository.getVideoOverview()

        start = int(request.args.get('start'))
        limit = int(request.args.get('limit'))
        count = len(videos)

        if count < start or limit < -1:
            return Response(
                response="No videos at this index or limit must be higher then 0",
                status=404
            )

        # make response
        response = {'start': start, 'limit': limit, 'count': count}
        # make URLs
        # make previous url
        if start == 0:
            response['previous'] = ''
        else:
            start_copy = max(0, start - limit)
            limit_copy = start
            response['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
        # make next url
        if start + limit > count:
            response['next'] = ''
        else:
            start_copy = start + limit
            response['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        # make first url
        response['first'] = url + '?start=1&limit=%d' % limit
        # make last url
        if count < limit:
            response['last'] = ''
        elif count % limit == 0:
            response['last'] = url + '?start=%d&limit=%d' % (count - limit, limit)
        else:
            response['last'] = url + '?start=%d&limit=%d' % (count - count % limit, limit)
        # finally extract result according to bounds
        response['results'] = videos[start:(start + limit)]

        return Response(
            response=response,
            status=200,
        )
