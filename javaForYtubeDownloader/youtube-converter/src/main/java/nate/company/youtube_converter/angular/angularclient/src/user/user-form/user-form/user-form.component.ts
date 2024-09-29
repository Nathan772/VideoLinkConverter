/*import { Component } from '@angular/core';

@Component({
  selector: 'app-user-form',
  standalone: true,
  imports: [],
  templateUrl: './user-form.component.html',
  styleUrl: './user-form.component.scss'
})
export class UserFormComponent {
généré automatiquement
}*/

/* repris du site baeldung */
import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../service/user.service';
import { User } from '../model/user';

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent {

  user: User;

  /*
  le user service du constructeur permet d'être utilisé
  pour sauvegarder le User offert.

  */
  constructor(
    private route: ActivatedRoute,
      private router: Router,
        private userService: UserService) {
    this.user = new User();
  }

  onSubmit() {
    //le goto , redirige vers le /users path
    this.userService.save(this.user).subscribe(result => this.gotoUserList());
  }

  gotoUserList() {
    this.router.navigate(['/users']);
  }
}
