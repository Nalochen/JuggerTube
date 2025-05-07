import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import {
  PaginatedVideosApiResponseModel,
  VideoApiResponseModel,
} from '../models/video-api-response.model';

@Injectable({
  providedIn: 'root',
})
export class VideosApiClient {
  constructor(private httpClient: HttpClient) {}

  public get(): Observable<VideoApiResponseModel[]> {
    return this.httpClient.get<VideoApiResponseModel[]>(
      '/api/video-frontend/get-video-overview'
    );
  }

  public getPaginatedVideos(
    start: number,
    limit: number
  ): Observable<PaginatedVideosApiResponseModel> {
    const params = new HttpParams().set('start', start).set('limit', limit);
    return this.httpClient.get<PaginatedVideosApiResponseModel>(
      '/api/video-frontend/get-paginated-videos',
      { params }
    );
  }
}
