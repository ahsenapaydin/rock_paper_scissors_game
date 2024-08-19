# Rock Paper Scissors Game

Bu Python projesi, klasik "Taş, Kağıt, Makas" oyununu simüle eden basit bir konsol oyunudur. Oyuncu ve bilgisayar arasında geçer ve oyuncu, bilgisayarın hareketine karşı taş, kağıt veya makas seçer. Belirli kurallara göre kazanan belirlenir.

## Nasıl Oynanır?

1. Oyunu başlattığınızda, ekranda taş, kağıt, makas seçenekleri gösterilecektir. 
2. Seçiminizi yapmak için taş, kağıt veya makas yazın ve `Enter` tuşuna basın.
3. Bilgisayar, rastgele bir seçim yapacak ve sonuç ekranda görünecektir.
4. Her iki oyuncunun puanı 2'ye ulaşana kadar oyun devam eder. 
5. Oyun sırasında "exit" yazarak oyundan çıkabilirsiniz.
6. Oyun bittikten sonra tekrar oynamak isteyip istemediğiniz sorulacaktır. "yes" ya da "no" olarak yanıtlayabilirsiniz.
   - Eğer hem oyuncu hem de bilgisayar tekrar oynamak isterse, oyun yeniden başlar.
   - Eğer oyuncu veya bilgisayar tekrar oynamak istemezse, oyun sona erer.

## Oyun Kuralları

- **Taş** kağıdı yener.
- **Kağıt** makası yener.
- **Makas** taşı yener.
- Aynı seçim yapılırsa, durum berabere biter ve puanlar değişmez.

## Gereksinimler

Bu oyunu çalıştırmak için sadece Python yüklü bir ortam yeterlidir. Ekstra bir bağımlılığa gerek yoktur.

## Oyunu Çalıştırmak

1. Python kurulu olduğundan emin olun.
2. `rock_paper_scissors.py` dosyasını terminal ya da komut istemcisi ile çalıştırın:

   ```bash
   python rock_paper_scissors.py
   ```

3. Oyunu oynamak için talimatları takip edin.

## Kod Açıklaması

- **actions_computer ve actions_player:** Bilgisayar ve oyuncu için oyun seçeneklerini içeren listeler.
- **random kütüphanesi:** Bilgisayarın rastgele seçim yapabilmesi için kullanılıyor.
- **play_again() fonksiyonu:** Oyunun ana döngüsü burada yer alır. Oyuncu ve bilgisayarın seçimleri değerlendirilir, puanlar güncellenir ve kazanan belirlenir.
- **Skor sistemi:** Oyuncu ve bilgisayarın puanları tutulur. 2 puana ulaşan ilk kişi oyunu kazanır.
- **Oyun tekrarı:** Oyun bittiğinde, hem oyuncunun hem de bilgisayarın tekrar oynayıp oynamak istemediği kontrol edilir.

## Katkıda Bulunma

Bu proje geliştirmeye açık olup, önerilerinizi ve katkılarınızı bekleriz. Herhangi bir hata bildirimi veya geliştirme fikri için lütfen bir "issue" oluşturun.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rock Paper Scissors Game

This Python project simulates the classic "Rock, Paper, Scissors" game. The game is played between a player and the computer, where the player chooses rock, paper, or scissors, and the winner is determined based on specific rules.

## How to Play?

1. When the game starts, the options rock, paper, and scissors will be displayed on the screen.
2. Type your choice (rock, paper, or scissors) and press `Enter`.
3. The computer will make a random choice, and the result will be shown on the screen.
4. The game continues until either the player or the computer scores 2 points.
5. You can exit the game at any time by typing "exit".
6. After the game ends, you will be asked if you want to play again. Respond with "yes" or "no".
   - If both the player and the computer want to play again, the game will restart.
   - If either the player or the computer doesn't want to play again, the game will end.

## Game Rules

- **Rock** beats scissors.
- **Paper** beats rock.
- **Scissors** beats paper.
- If both players make the same choice, the round is a tie, and no points are awarded.

## Requirements

To run this game, all you need is a Python environment. No additional dependencies are required.

## Running the Game

1. Make sure Python is installed.
2. Run the `rock_paper_scissors.py` file using the terminal or command prompt:

   ```bash
   python rock_paper_scissors.py
   ```

3. Follow the on-screen instructions to play the game.

## Code Explanation

- **actions_computer and actions_player:** Lists containing the game options for the computer and player.
- **random library:** Used to allow the computer to make a random choice.
- **play_again() function:** This is the main loop of the game. It evaluates the player's and computer's choices, updates the scores, and determines the winner.
- **Scoring system:** The scores of the player and computer are tracked. The first to reach 2 points wins the game.
- **Game repetition:** After the game ends, it checks whether both the player and computer want to play again.

## Contributing

This project is open to improvements, and we welcome your suggestions and contributions. Please create an "issue" for any bug reports or ideas for enhancements.

## License

This project is licensed under the MIT License. For more information, see the `LICENSE` file.
