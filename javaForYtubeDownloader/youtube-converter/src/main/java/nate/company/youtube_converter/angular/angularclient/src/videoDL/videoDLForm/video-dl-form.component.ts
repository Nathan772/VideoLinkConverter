import { Component, OnInit } from '@angular/core';
import { Video } from '../video';
import { VideoDLServiceService } from '../videoDLService/video-dlservice.service'
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-video-dl-form',
  templateUrl: './video-dl-form.component.html',
  styleUrl: './video-dl-form.component.scss'
})
export class VideoDLFormComponent implements OnInit {

  router:Router;
  videoService:VideoDLServiceService;
  video:Video;

  /*
  le user service du constructeur permet d'être utilisé
  pour sauvegarder la vidéo
  */
  constructor(routerParam: Router,service: VideoDLServiceService) {
    this.router = routerParam;
    this.videoService=service;
    /*nécessaire même si sera remplacé
    car cela correspond aux valeurs par défaut de l'utilisateur
    même si l'id pourrait causer un conflit,
    en pratique ce n'est pas le cas
    car il est aussi automatiquement
    remplacé par la base de donnée
    par le suivant du serial !!
    */
    this.video = {id:"5", link:""}
  }
  registerNewVideo() {
    //le goto , redirige vers le /users path
    /*
    on appelle le save de user-service
    pour sauvegarder en base en appelant en fait du java
    */
    this.videoService.save(this.video).subscribe(
      result => this.gotoVideoList());
  }

  gotoVideoList() {
      this.router.navigate(['/videos']);
    }

  gotoEntryPage() {
    this.router.navigate(['/entry']);
  }

  ngOnInit(){}

}
