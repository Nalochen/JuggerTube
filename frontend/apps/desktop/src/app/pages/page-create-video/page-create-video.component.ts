import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {
  FormControl,
  FormGroup,
  FormsModule,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';
import { Router } from '@angular/router';

import {
  UiButtonColorEnum,
  UiButtonComponent,
} from '../../ui-button/ui-button.component';
import {
  UiInputComponent,
  UiInputDirectionEnum,
  UiInputTypeEnum,
} from '../../ui-input/ui-input.component';
import {
  GameSystemTypesEnum,
  VideoCategoriesEnum,
  WeaponTypesEnum,
} from '@frontend/video-data';

export const createVideoForm = new FormGroup<{
  name: FormControl<string>;
  videoLink: FormControl<string>;
  channelLink: FormControl<string>;
  category: FormControl<VideoCategoriesEnum | null>;
  uploadDate: FormControl<string>;
  dateOfRecording: FormControl<string>;
  topic: FormControl<string>;
  guests: FormControl<string>;
  weaponType: FormControl<WeaponTypesEnum | null>;
  gameSystem: FormControl<GameSystemTypesEnum | null>;
  tournamentId: FormControl<number>;
  teamOneId: FormControl<number>;
  teamTwoId: FormControl<number>;
  comment: FormControl<string>;
}>({
  name: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required, Validators.email],
  }),
  videoLink: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  channelLink: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  category: new FormControl(null, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  uploadDate: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  dateOfRecording: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  topic: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  guests: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
  weaponType: new FormControl(null, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  gameSystem: new FormControl(null, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  tournamentId: new FormControl(0, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  teamOneId: new FormControl(0, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  teamTwoId: new FormControl(0, {
    nonNullable: true,
    validators: [Validators.required],
  }),
  comment: new FormControl('', {
    nonNullable: true,
    validators: [Validators.required],
  }),
});

export enum AdditionalFieldsEnum {
  GAME_SYSTEM = 'gameSystem',
  WEAPON_TYPE = 'weaponType',
  TOPIC = 'topic',
  GUESTS = 'guests',
  TEAMS = 'teams',
  TOURNAMENT = 'tournament',
}

@Component({
  imports: [
    CommonModule,
    FormsModule,
    UiButtonComponent,
    UiInputComponent,
    ReactiveFormsModule,
  ],
  standalone: true,
  templateUrl: './page-create-video.component.html',
  styleUrl: './page-create-video.component.less',
})
export class PageCreateVideoComponent implements OnInit {
  constructor(private router: Router) {}

  public ngOnInit() {
    this.form.controls.category.valueChanges.subscribe(
      (value: VideoCategoriesEnum | null) => {
        if (!value) {
          this.additionalFields = [];
          return;
        }

        switch (value) {
          case VideoCategoriesEnum.REPORTS:
            this.additionalFields = [AdditionalFieldsEnum.TOPIC];
            break;
          case VideoCategoriesEnum.HIGHLIGHTS:
            this.additionalFields = [
              AdditionalFieldsEnum.TOPIC,
              AdditionalFieldsEnum.GUESTS,
              AdditionalFieldsEnum.TOURNAMENT,
            ];
            break;
          case VideoCategoriesEnum.SPARBUILDING:
            this.additionalFields = [
              AdditionalFieldsEnum.WEAPON_TYPE,
              AdditionalFieldsEnum.TOPIC,
              AdditionalFieldsEnum.GUESTS,
            ];
            break;
          case VideoCategoriesEnum.MATCH:
            this.additionalFields = [
              AdditionalFieldsEnum.TOURNAMENT,
              AdditionalFieldsEnum.GAME_SYSTEM,
              AdditionalFieldsEnum.TEAMS,
            ];
            break;
          case VideoCategoriesEnum.OTHER:
          case VideoCategoriesEnum.PODCAST:
            this.additionalFields = [
              AdditionalFieldsEnum.TOPIC,
              AdditionalFieldsEnum.GUESTS,
            ];
            break;
          case VideoCategoriesEnum.TRAINING:
            this.additionalFields = [
              AdditionalFieldsEnum.GAME_SYSTEM,
              AdditionalFieldsEnum.WEAPON_TYPE,
              AdditionalFieldsEnum.TOPIC,
            ];
            break;
          case VideoCategoriesEnum.AWARDS:
            this.additionalFields = [AdditionalFieldsEnum.TOURNAMENT];
            break;
          default:
            this.additionalFields = [];
        }
      }
    );
  }

  protected readonly form = createVideoForm;
  protected additionalFields: AdditionalFieldsEnum[] = [];

  public onSubmit(): void {
    if (!this.form.valid) {
      this.markAllFieldsAsTouched();
      return;
    }

    //this.videoService.create(this.form.value);

    this.form.reset();

    this.router.navigate(['/']);
  }

  private markAllFieldsAsTouched(): void {
    Object.keys(this.form.controls).forEach((field) => {
      const control = this.form.get(field);
      if (control instanceof FormControl) {
        control.markAsTouched({ onlySelf: true });
      }
    });
  }

  public tournamentOptions = [];
  public teamOptions = [];

  protected readonly UiButtonColorEnum = UiButtonColorEnum;
  protected readonly UiInputTypeEnum = UiInputTypeEnum;
  protected readonly UiInputDirectionEnum = UiInputDirectionEnum;
  protected readonly AdditionalFieldsEnum = AdditionalFieldsEnum;
  protected readonly Object = Object;
  protected readonly VideoCategoriesEnum = VideoCategoriesEnum;
  protected readonly WeaponTypesEnum = WeaponTypesEnum;
  protected readonly GameSystemTypesEnum = GameSystemTypesEnum;
}
