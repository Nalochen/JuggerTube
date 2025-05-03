import { Injectable, Signal } from '@angular/core';

import { Observable } from 'rxjs';

import { Store } from '@ngrx/store';

import {loadNextVideos, loadPaginatedVideosAction, loadVideosAction} from '../store/actions/videos.actions';
import { VideosStateAware } from '../store/models/videos-state.model';
import { videosDataSelector } from '../store/selectors/videos-data.selector';
import { videosRequestStateSelector } from '../store/selectors/videos-request-state.selector';
import { RequestStateEnum } from '@frontend/api';
import { SingletonGetter } from '@frontend/cache';
import { VideoApiResponseModel } from '@frontend/video-data';
import {paginatedVideosDataSelector} from '../store/selectors/paginated-videos-data.selector';
import {totalCountVideosDataSelector} from '../store/selectors/total-count-videos-data.selector';

@Injectable({ providedIn: 'root' })
export class VideosDataService {
  @SingletonGetter()
  public get videos(): Signal<VideoApiResponseModel[]> {
    return this.store$.selectSignal(videosDataSelector);
  }

  @SingletonGetter()
  public get paginatedVideos(): Signal<VideoApiResponseModel[]> {
    return this.store$.selectSignal(paginatedVideosDataSelector);
  }

  @SingletonGetter()
  public get totalCountVideos(): Signal<number> {
    return this.store$.selectSignal(totalCountVideosDataSelector);
  }

  @SingletonGetter()
  public get videoRequestState$(): Observable<RequestStateEnum> {
    return this.store$.select(videosRequestStateSelector);
  }

  constructor(private readonly store$: Store<VideosStateAware>) {}

  public loadVideos(): void {
    this.store$.dispatch(loadVideosAction());
  }

  public loadPaginatedVideos(start: number, limit: number): void {
    this.store$.dispatch(loadPaginatedVideosAction({ start: start, limit: limit }));
  }

  public loadNextVideos(start: number, limit: number): void {
    this.store$.dispatch(loadNextVideos({ start: start, limit: limit }));
  }
}
