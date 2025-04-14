import { Injectable, Signal } from '@angular/core';

import { Observable } from 'rxjs';

import { Store } from '@ngrx/store';

import { loadVideosAction } from '../store/actions/videos.actions';
import { VideosStateAware } from '../store/models/videos-state.model';
import { videosDataSelector } from '../store/selectors/videos-data.selector';
import { videosRequestStateSelector } from '../store/selectors/videos-request-state.selector';
import { RequestStateEnum } from '@frontend/api';
import { SingletonGetter } from '@frontend/cache';
import { VideoApiResponseModel } from '@frontend/data-domain-videos';

@Injectable({ providedIn: 'root' })
export class VideosDataService {
  @SingletonGetter()
  public get videos(): Signal<VideoApiResponseModel[]> {
    return this.store$.selectSignal(videosDataSelector);
  }

  @SingletonGetter()
  public get videoRequestState$(): Observable<RequestStateEnum> {
    return this.store$.select(videosRequestStateSelector);
  }

  constructor(private readonly store$: Store<VideosStateAware>) {}

  public loadVideos(): void {
    this.store$.dispatch(loadVideosAction());
  }
}
