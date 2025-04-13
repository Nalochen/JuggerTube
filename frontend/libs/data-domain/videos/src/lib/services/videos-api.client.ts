import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import {Observable} from "rxjs";
import {VideoApiResponseModel} from "../models/video-api-response.model";

const apiUrl = '/api/video-frontend/get-video-overview';

@Injectable({
  providedIn: 'root',
})
export class VideosApiClient {
  constructor(private httpClient: HttpClient) {}

  public get(): Observable<VideoApiResponseModel[]> {
    return this.httpClient
      .get<VideoApiResponseModel[]>(apiUrl)
  }
}
