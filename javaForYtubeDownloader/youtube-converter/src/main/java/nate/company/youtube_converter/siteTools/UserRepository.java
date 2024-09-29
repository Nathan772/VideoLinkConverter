package nate.company.youtube_converter.siteTools;

import nate.company.youtube_converter.controller.UserController;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 *
 * interface créée manuellement.
 * Elle est nécessaire pour pouvoir utiliser les méthodes associées à la BDD,
 * (JPA)CRUD, c'est à dire : Create, READ, UPDATE, DELETE
 */
@Repository
@Component
public interface UserRepository extends JpaRepository<User,Long> {


}
