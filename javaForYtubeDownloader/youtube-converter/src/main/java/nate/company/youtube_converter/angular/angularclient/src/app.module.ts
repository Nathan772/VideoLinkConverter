/*
généré manuellement + baeldung
+ moi
*/

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app/app-routing.module';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app/app.component';
import { UserListComponent } from './user/user_list/user-list.component';
import { UserFormComponent } from './user/user_form/user-form.component';
import { UserService } from './user/user_service/user-service.service';
import {RouterModule} from '@angular/router';

@NgModule({
   declarations: [
      AppComponent,
      UserListComponent,
      UserFormComponent,
    ],
  imports: [
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      FormsModule,
      RouterModule
    ],
  providers: [UserService],
  bootstrap:[AppComponent],
})
export class AppModule { }
