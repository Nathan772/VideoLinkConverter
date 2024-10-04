import { Component, OnInit } from '@angular/core';
import { Video } from '../video'
import { ActivatedRoute, Router } from '@angular/router';
import { VideoDLServiceService } from '../videoDLService/video-dlservice.service';
@Component({
  selector: 'app-video-dlpage',
  templateUrl: './video-dlpage.component.html',
  styleUrl: './video-dlpage.component.scss'
})
export class VideoDLPageComponent implements OnInit {

  videoService:VideoDLServiceService;
  router:Router;

  constructor(routerParam: Router, service: VideoDLServiceService) {
      this.videoService = service;
      this.router = routerParam;
  }

  //utiliser les router pour associer
  //des pages associés à des comptes users
  gotoVideoPage(){
      this.router.navigate(['/videos']);
  }

  ngOnInit(){}
}
