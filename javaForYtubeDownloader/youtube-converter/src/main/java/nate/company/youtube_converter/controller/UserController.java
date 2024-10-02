package nate.company.youtube_converter.controller;

import nate.company.youtube_converter.siteTools.User;
import nate.company.youtube_converter.siteTools.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

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
public class UserController {

    /*
    constructeur nécessaire pour l'API REST
    créée par moi-même en s'inspirant du lien
    baledung ci-dessus.
     */
    //standard constructors

    private final UserRepository userRepository;

    /*
    constructeur créé par moi-même qui se remplit avec un paramètre de type UserRepo...
    C'est Spring qui gérera lui-même l'ajout/la création de l'argument lors de l'appel
     */
    public UserController(UserRepository userRepository){
        Objects.requireNonNull(userRepository);
        this.userRepository = userRepository;
    }

    /**
     * this method retrieves all the users from the database
     * @return
     */
    //@RequestMapping("/users")
    @GetMapping("/users")
    public List<User> getUsers(){
        return (List<User>) userRepository.findAll();
    }

    /**
     * the add user add a new user in the data based, when this one
     * is passed through the request body
     * normally we would need to add controller implementation, in order to check if user data is validate or not
     * but to keep it simple we didnt did it here but you can find how in the baledung page
     * at "Spring boot validation" click link.
     * @param user
     */
    @PostMapping("/users")
    void addUser(@RequestBody User user){
        userRepository.save(user);
    }


}
