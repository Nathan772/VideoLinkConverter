import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Video } from '../video';

@Injectable({
  providedIn: 'root'
})
export class VideoDLServiceService {

  private videosUrl: string;

    constructor(private http: HttpClient) {
      //url toward the link to the backend
      // associated to videos database page
      this.videosUrl = 'http://localhost:8080/videos';
    }

    /**
     retrive all the videos downloaded so far by every users
     */
    public findAll(): Observable<Video[]> {
      return this.http.get<Video[]>(this.videosUrl);
    }

  /* sauvegarde en base une vidéo choisie
  la méthode save réalise une requête avec
  l'@ "'http://localhost:8080/videos'"
  du constructor.
  Elle est liée à "addVideo"  du
  VideoController.java

  */
    public save(video: Video) {
      console.log("On sauvegarde une nouvelle vidéo : "+video);
      return this.http.post<Video>(this.videosUrl, video);
    }

  /**
   cette méthode permet la suppresion d'un user.
   Elle est liée à
   removeUser de UserController.java.
   la méthode delete réalise une requête avec l'@ :

  http://localhost:8080/user
   */
    public delete(video: Video) {
      console.log("On supprime une video : "+video);
      console.log("la vidéo a pour id : "+video.id)
      //use the url associated deleteMapping of UserController
      return this.http.delete(this.videosUrl+"/delete/"+video.id);
      //censé marcher : "http://localhost:8080/users/delete/302"
    }
}
