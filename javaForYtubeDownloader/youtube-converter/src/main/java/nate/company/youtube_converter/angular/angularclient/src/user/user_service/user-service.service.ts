import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from '../model/user';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class UserService {

  private usersUrl: string;

  constructor(private http: HttpClient) {
    this.usersUrl = 'http://localhost:8080/users';
  }

  /* récupère les users que l'on souhaite prendre depuis
  la base */
  public findAll(): Observable<User[]> {
    return this.http.get<User[]>(this.usersUrl);
  }

/* sauvegarde en base un utilisateur choisit
la méthode save réalise une requête avec
l'@ "'http://localhost:8080/users'"
du constructor
*/
  public save(user: User) {
    return this.http.post<User>(this.usersUrl, user);
  }
}
