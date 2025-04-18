import {
  animate,
  state,
  style,
  transition,
  trigger,
} from '@angular/animations';
import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

import { UiRedirectComponent } from '../../ui-redirect/ui-redirect.component';
import { UiTagComponent } from '../../ui-tag/ui-tag.component';
import {
  GameSystemTypesEnum,
  VideoCategoriesEnum,
  WeaponTypesEnum,
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
  public video = {
    id: 1,
    name: 'Testvideo 2',
    category: VideoCategoriesEnum.HIGHLIGHTS,
    videoLink: 'https://www.youtube.com/embed/f27SC622NvE?si=tkrwZRDEUWp8bLy0',
    comment: 'richtig wichtiger comment',
    gameSystem: GameSystemTypesEnum.NRW,
    weaponType: WeaponTypesEnum.LONGSWORD,
    topic: 'Have fun',
    guests: 'Leander',
    uploadDate: '10-03-2028',
    dateOfRecording: '10-03-2028',
    channelName: 'ae²ae³',
    channelLink: 'https://www.youtube.com/@ae²ae³',
    tournament: {
      id: 1,
      name: 'Best tournament',
      city: 'Berlin',
      startDate: '10-03-2028',
      endDate: '10-03-2028',
      jtrLink: 'https://youtu.be/f27SC622NvE',
    },
    teamOne: {
      id: 1,
      name: 'Rigor Mortis',
      city: 'Berlin',
    },
    teamTwo: {
      id: 2,
      name: 'Jugger Basilisken',
      city: 'Hamburg',
    },
  };

  public showTournamentDetails: boolean = false;
  public showTeamOneDetails: boolean = false;
  public showTeamTwoDetails: boolean = false;
}
