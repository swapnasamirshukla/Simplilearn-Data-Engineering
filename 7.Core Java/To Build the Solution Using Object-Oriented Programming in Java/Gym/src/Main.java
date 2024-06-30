import java.util.ArrayList;
import java.util.Scanner;

class Participant {
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

class Batch {
    private String name;
    private ArrayList<Participant> participants;

    public Batch(String name) {
        this.name = name;
        participants = new ArrayList<>();
    }

    public void addParticipant(Participant participant) {
        participants.add(participant);
    }

    public void start() {
        for (Participant participant : participants) {
            participant.receiveMessage("Batch " + name + " has started.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter the name of the batch:");
        String batchName = scanner.nextLine();
        Batch batch = new Batch(batchName);

        System.out.println("Enter the number of participants:");
        int numParticipants = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        for (int i = 0; i < numParticipants; i++) {
            System.out.println("Enter participant name " + (i + 1) + ":");
            String participantName = scanner.nextLine();
            Participant participant = new Participant(participantName);
            batch.addParticipant(participant);
        }

        batch.start();
        scanner.close();
    }
}

