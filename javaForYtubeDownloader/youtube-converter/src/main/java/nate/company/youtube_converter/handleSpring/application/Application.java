package nate.company.youtube_converter.handleSpring.application;

/* import proposé au clique sur les différentes annotations en rouge

 */
import nate.company.youtube_converter.handleSpring.application.repository.siteTools.User;
import nate.company.youtube_converter.handleSpring.application.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

import java.util.stream.Stream;

/*ç
créé moi-même copie du code de la page baledung.com :
ajoutés manuellement
 */

//@Profile("MainPrincipal")
//Le exclude retire l'utilisation de la base de données
//il faudra le désactiver si on veut utiliser la bdd plus tard
@SpringBootApplication
/*
nécessaire pour résoudre :
Parameter 0 of method init in nate.company.youtube_converter.application.Application
required a bean of type 'nate.company.youtube_converter.handleSpring.application.repository.UserRepository' that could not be found.
 */
//le component scan va chercher dans ce répertoire et ses s
//sous répertoire les éléments recherchés (ici UserRepository)
@ComponentScan({"nate/company/youtube_converter"})
public class Application {
git
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @Bean
    CommandLineRunner init(UserRepository userRepository) {
        return args -> {
            Stream.of("John", "Julie", "Jennifer", "Helen", "Rachel").forEach(name -> {
                User user = new User(name, name.toLowerCase() + "@domain.com");
                userRepository.save(user);
            });
            userRepository.findAll().forEach(System.out::println);
        };
    }
}
