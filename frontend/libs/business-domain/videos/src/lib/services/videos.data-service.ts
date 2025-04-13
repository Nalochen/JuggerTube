import {Injectable} from "@angular/core";
import {Observable} from "rxjs";
import {VideoApiResponseModel} from "@frontend/data-domain-videos";
import {Store} from "@ngrx/store";
import {videosDataSelector} from "../store/selectors/videos-data.selector";
import {SingletonGetter} from "@frontend/cache";
import {RequestStateEnum} from "@frontend/api";
import {videosRequestStateSelector} from "../store/selectors/videos-request-state.selector";
import {VideosStateAware} from "../store/models/videos-state.model";

@Injectable({ providedIn: 'root' })
export class VideosDataService {
  @SingletonGetter()
  public get videos$(): Observable<VideoApiResponseModel[]> {
    return this.store$.select(videosDataSelector);
  }

  @SingletonGetter()
  public get videoRequestState$(): Observable<RequestStateEnum> {
    return this.store$.select(videosRequestStateSelector);
  }

  constructor(private readonly store$: Store<VideosStateAware>) {}
}
