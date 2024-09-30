package nate.company.youtube_converter.handleSpring.application.repository;

import nate.company.youtube_converter.handleSpring.application.repository.siteTools.User;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 *
 * interface créée manuellement.
 * Elle est nécessaire pour pouvoir utiliser les méthodes associées à la BDD,
 * (JPA)CRUD, c'est à dire : Create, READ, UPDATE, DELETE
 */
//@Component
@ComponentScan({"nate/company/youtube_converter"})
@Repository
public interface UserRepository extends JpaRepository<User,Long> {


}
