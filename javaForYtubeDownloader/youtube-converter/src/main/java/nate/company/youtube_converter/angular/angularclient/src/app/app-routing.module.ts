/* fichier créé et remplit à la main + via baeldung */
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { UserListComponent } from '../user/user_list/user-list.component';
import { UserFormComponent } from '../user/user_form/user-form.component';
import { UserService } from '../user/user_service/user-service.service';

/*
ce tableau indique quel composant afficher selon
le chemin web "path" choisit par le user
*/
const routes: Routes = [
  { path: 'users', component: UserListComponent },
  { path: 'adduser', component: UserFormComponent }
];

/*
@Component({
  selector:'app-routing-user'
  })*/
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
/*
@Injectable({
  providedIn:'root'})*/
export class AppRoutingModule { }
