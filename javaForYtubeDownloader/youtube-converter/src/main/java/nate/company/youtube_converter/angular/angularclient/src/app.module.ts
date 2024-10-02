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
  imports: [
      BrowserModule,
      AppRoutingModule,
      HttpClientModule,
      FormsModule,
    ],

  declarations: [
    AppComponent,
    UserListComponent,
    UserFormComponent,
  ],

  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
