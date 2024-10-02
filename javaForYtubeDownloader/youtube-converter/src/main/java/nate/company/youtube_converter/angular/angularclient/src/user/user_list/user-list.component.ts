/*
auto-généré
import { Component } from '@angular/core';

@Component({
  selector: 'app-user-list',
  standalone: true,
  imports: [],
  templateUrl: './user-list.component.html',
  styleUrl: './user-list.component.scss'
})
export class UserListComponent {

}*/

import { Component, OnInit } from '@angular/core';
import { User } from '../user';
import { UserService } from '../user_service/user-service.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.scss']
})

/*
certains message d'erreurs
peuvent n'avoir aucun rapport avec
la vraie cause de l'erreur,
c'est donc au user de trouver en tatonnant
et en cherchant ce qui est inhabituel.
J'ai ainsi eux un msg
qui parlait d'une accolade,
alors que les causes de l'erreur étaient
la présence du mot "var" avant le nom
de la variable et aussi un
constructeur de service qui n'utilisait pas
le mot "this" + le paramètre
service qui était privé
*/
export class UserListComponent implements OnInit {

  users: User[];
  userService:UserService;


  constructor(service: UserService) {
    this.users = [];
    this.userService = service;
    this.userService.findAll().subscribe(data => {
          this.users = data;
        });
  }

  ngOnInit() {
    //stocke les users récupérés
    // dans this.users

  }
}
