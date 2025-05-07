import {
  animate,
  state,
  style,
  transition,
  trigger,
} from '@angular/animations';
import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';

import { UiRedirectComponent } from '../../ui-redirect/ui-redirect.component';
import { UiTagComponent } from '../../ui-tag/ui-tag.component';
import { VideosDataService } from '@frontend/video';
import {
  VideoApiResponseModel
} from '@frontend/video-data';

@Component({
  imports: [CommonModule, UiRedirectComponent, RouterLink, UiTagComponent],
  standalone: true,
  templateUrl: './page-video-details.component.html',
  styleUrl: './page-video-details.component.less',
  animations: [
    trigger('slideDown', [
      state('hidden', style({ height: '0px', overflow: 'hidden', opacity: 0 })),
      state('visible', style({ height: '*', overflow: 'hidden', opacity: 1 })),
      transition('hidden <=> visible', [animate('300ms ease-in-out')]),
    ]),
  ],
})
export class PageVideoDetailsComponent {
  public video: VideoApiResponseModel | undefined = undefined;

  public showTournamentDetails: boolean = false;
  public showTeamOneDetails: boolean = false;
  public showTeamTwoDetails: boolean = false;

  constructor(
    private route: ActivatedRoute,
    private videosDataService: VideosDataService
  ) {
    const videoId = Number(this.route.snapshot.paramMap.get('id'));
    this.video = this.videosDataService.getVideoById(videoId);
    console.log(this.video);
  }
}
