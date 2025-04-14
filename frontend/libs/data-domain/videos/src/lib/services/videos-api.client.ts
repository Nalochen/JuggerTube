import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';

import { VideoApiResponseModel } from '../models/video-api-response.model';

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
}
