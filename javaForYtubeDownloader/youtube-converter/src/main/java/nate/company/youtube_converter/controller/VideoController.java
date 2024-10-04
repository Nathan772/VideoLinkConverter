package nate.company.youtube_converter.controller;
import nate.company.youtube_converter.siteTools.User;
import nate.company.youtube_converter.siteTools.UserRepository;
import nate.company.youtube_converter.siteTools.Video;
import nate.company.youtube_converter.siteTools.VideoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.lang.annotation.Repeatable;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/* cette
partie a été écrite manuellement il faut tjrs se référer à la page
https://www.baeldung.com/spring-boot-angular-web
 */
@RestController
/*
C'est le front qui est en 4200, mais cela permet justement de connecter le back au front
 */
//@CrossOrigin(origins="https://localhost:4200", maxAge =3600)
/*
permet de résoudre le problème de
"No Access-control-allow-origin"
cors policy error
 */
@CrossOrigin("*")
public class VideoController {

    /*
    constructeur nécessaire pour l'API REST
    créée par moi-même en s'inspirant du lien
    baledung ci-dessus.
     */
    //standard constructors

    private final VideoRepository videoRepository;

    /*
    constructeur créé par moi-même qui se remplit avec un paramètre de type UserRepo...
    C'est Spring qui gérera lui-même l'ajout/la création de l'argument lors de l'appel
     */
    public VideoController(VideoRepository videoRepository){
        Objects.requireNonNull(videoRepository);
        this.videoRepository = videoRepository;
    }

    /**
     * this method retrieves all the users from the database
     * elle est liée à la méthode "findAll" présente dans
     * user-service.service.ts
     * d'où le fait qu'elle appelle findAll()
     * @return
     */
    //@RequestMapping("/users")
    @GetMapping("/videos")
    public List<Video> getVideos(){
        return (List<Video>) videoRepository.findAll();
    }

    /**
     * the addVideo add a new video in the data based, when this one
     * is passed through the request body
     * normally we would need to add controller implementation, in order to check if user data is validate or not
     * but to keep it simple we didnt did it here but you can find how in the baledung page
     * at "Spring boot validation" click link.
     * Elle est liée à la méthode "save" de vide-dlservice.service.ts
     * d'où le fait qu'elle appelle save
     * @param video
     */
    @PostMapping("/videos")
    public void addVideo(@RequestBody Video video){
        System.out.println(" on ajoute la vidéo : "+video);
        videoRepository.save(video);
    }




    /**
     * the addVideo add a new video in the data based, when this one
     * is passed through the request body
     * normally we would need to add controller implementation, in order to check if user data is validate or not
     * but to keep it simple we didnt did it here but you can find how in the baledung page
     * at "Spring boot validation" click link.
     * Elle est liée à la méthode "save" de vide-dlservice.service.ts
     * d'où le fait qu'elle appelle save
     * @param video
     */
    @PostMapping("/videos")
    public ResponseEntity<String> downloadVideo(@RequestBody Video video){
        System.out.println(" on télécharge la vidéo : "+video);
        var videoName = "backOn";
        return ResponseEntity.status(HttpStatus.ACCEPTED).body(videoName);

    }











    /**
     * this method enables to delete a user based on their id.
     * it is linked to delete from user-service.service hence the call to delete
     * @param id
     * the id of the user you want to remove
     */

    /**
     * remove method for videos.
     * Even if the mapping starts by delete, it starts implicitly by
     * You can try a request with postman to check if it actually works.
     * @param id
     * @return
     */

    @DeleteMapping("videos/delete/{id}")
    public ResponseEntity<String> removeVideo(@PathVariable String id){
        var videoIdLong = Long.parseLong(id);
        //var userIdLong = user.getId();
        System.out.println("on supprime le user avec l'id : "+videoIdLong);
        videoRepository.deleteById(videoIdLong);
        /* renvoyer un élément
        est indispensable et est nécessaire, sinon
        la suppression ne fonctionne pas.
        le retour d'un objet d'un type différent de ResponseEntity n'est pas accepté
        et provoquera un échec de la suppression
         */
        return ResponseEntity.noContent().build();
    }

    /*
    @DeleteMapping("/users/{id}")
    void removeUser(@RequestBody User user){
        //var userIdLong = Long.parseLong(user.getId());
        var userIdLong = user.getId();
        System.out.println("on supprime le user avec l'id : "+userIdLong);
        userRepository.delete(user);
    }*/


}
