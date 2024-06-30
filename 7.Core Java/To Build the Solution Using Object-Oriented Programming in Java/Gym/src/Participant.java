
public class Participant {
	private String name;

    public Participant(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void receiveMessage(String message) {
        System.out.println(name + " received message: " + message);
    }
}
