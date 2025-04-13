import { NgModule } from "@angular/core";

import { EffectsModule } from '@ngrx/effects';
import { StoreModule } from '@ngrx/store';
import {LoadVideosEffects} from "./effects/load-videos.effects";
import {videosFeatureKey} from "./models/videos-state.model";
import {videosReducer} from "./reducers/videos.reducer";

@NgModule({
  imports: [
    EffectsModule.forFeature([
      LoadVideosEffects
    ]),
    StoreModule.forFeature(videosFeatureKey, videosReducer),
  ],
})
export class ComparisonStoreModule {}
