import { ActionReducer, ActionReducerMap, MetaReducer } from '@ngrx/store';
import { localStorageSync } from 'ngrx-store-localstorage';

import { VideosState } from '../models/videos-state.model';
import { videosReducer } from '@frontend/business-domain-videos';

export interface State {
  videoOverview: VideosState;
}

export const reducers: ActionReducerMap<State> = {
  videoOverview: videosReducer,
};

export function localStorageSyncReducer(
  // eslint-disable-next-line
  reducer: ActionReducer<any>
  // eslint-disable-next-line
): ActionReducer<any> {
  return localStorageSync({
    keys: ['videosReducer'],
    storage: localStorage,
    rehydrate: true,
  })(reducer);
}

export const metaReducers: MetaReducer<State>[] = [localStorageSyncReducer];
