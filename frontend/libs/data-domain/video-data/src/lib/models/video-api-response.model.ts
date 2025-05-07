import { GameSystemTypesEnum } from '../enums/game-system-types.enum';
import { VideoCategoriesEnum } from '../enums/video-categories.enum';
import { WeaponTypesEnum } from '../enums/weapon-types.enum';

export interface Channel {
  name: string;
  link: string;
}

export interface Tournament {
  name: string;
  city: string;
  startDate: Date;
  endDate: Date;
  jtrLink: string;
}

export interface Team {
  name: string;
  city: string;
}

export interface VideoApiResponseModel {
  id: number;
  name: string;
  category: VideoCategoriesEnum;
  videoLink: string;
  uploadDate: Date;
  comment: string;
  dateOfRecording: Date;
  gameSystem: GameSystemTypesEnum;
  weaponType: WeaponTypesEnum;
  topic: string;
  guests: string;
  channel: Channel;
  tournament: Tournament;
  teamOne: Team;
  teamTwo: Team;
}

export interface PaginatedVideosApiResponseModel {
  count: number;
  next: string | null;
  previous: string | null;
  results: VideoApiResponseModel[];
}
