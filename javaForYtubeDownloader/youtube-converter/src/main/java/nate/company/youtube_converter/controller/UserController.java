package nate.company.youtube_converter.controller;

import nate.company.youtube_converter.siteTools.User;
import nate.company.youtube_converter.siteTools.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/* cette
partie a été écrite manuellement il faut tjrs se référer à la page
https://www.baeldung.com/spring-boot-angular-web
se fier à cette page plutôt qu'à celle de react X spring
 */
@RestController
//@RequestMapping("/users")
@CrossOrigin(origins="https://localhost:4200")
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
    @GetMapping
    public List<User> getUsers(){
        return (List<User>) userRepository.findAll();
    }

    /**
     * this method retrieves a user based on his id from the database
     * @param id
     * the user's id that enables to retrieve the user you're interested in.
     */
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id){
       return userRepository.findById(id).orElseThrow(RuntimeException::new);
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

    /**
     * (inspired by baeldung method spring + react page)
     * this method enables to save a user in database
     * @param user
     * the user you want to save in data base
     * @return
     * the response either creation worked or not
     * @throws URISyntaxException
     */
    @PostMapping
    public ResponseEntity createUser(@RequestBody User user) throws URISyntaxException {
        User savedClient = userRepository.save(user);
        return ResponseEntity.created(new URI("/users/" + savedClient.getId())).body(savedClient);
    }

    /**
     *
     * this method enable to change user's information based on his id
     * and his new information set up in their object.
     * @param id
     * @param user
     * @return
     */
    @PutMapping("/{id}")
    public ResponseEntity updateUser(@PathVariable Long id, @RequestBody User user) {
        User currentClient = userRepository.findById(id).orElseThrow(RuntimeException::new);
        currentClient.setName(user.getName());
        currentClient.setEmail(user.getEmail());
        currentClient = userRepository.save(user);

        return ResponseEntity.ok(currentClient);
    }

    /**
     *
     * this method remove a user from the database.
     * @param id
     * the user's id that enable to select the user you want to remove.
     * @return
     * the response : either it worked or not
     */
    @DeleteMapping("/{id}")
    public ResponseEntity deleteUser(@PathVariable Long id) {
        userRepository.deleteById(id);
        return ResponseEntity.ok().build();
    }


}
