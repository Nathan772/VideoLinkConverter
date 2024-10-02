package nate.company.youtube_converter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Profile;

@SpringBootApplication
@Profile("YconverterMain")
public class YoutubeConverterApplication {

	public static void main(String[] args) {
		SpringApplication.run(YoutubeConverterApplication.class, args);
	}

}
