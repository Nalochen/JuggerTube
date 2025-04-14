import { GameSystemTypesEnum } from '../enums/game-system-types.enum';
import { VideoCategoriesEnum } from '../enums/video-categories.enum';
import { WeaponTypesEnum } from '../enums/weapon-types.enum';

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
  channelName: string;
  tournamentName: string;
  teamOneName: string;
  teamTwoName: string;
}
