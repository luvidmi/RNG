#include <iostream>
#include <fstream>
#include <vector>

void generator(char*filenameNames, char*filenameWords, )
{
    std::ifstream finWord;
    std::ifstream finName;
    finWord.open(filenameNames, std::ios::in);
    if (!finWord)
    {
        std::cout<<"Нет исходного файла";
    }
    finName.open(filenameWords, std::ios::in);
    if (!finName)
    {
        std::cout<<"Нет исходного файла";
    }
    char word;
    char name;
    for (int i = 0; i<200; i++)
    {
        while (word >> namesWords[i][0]){

        }
        
    }
}

void printNames(int howmuch)
{

}

void change()
{

}


int main(){
    std::vector<char> massWords;
    std::vector<char> massNames;
    bool isGenerated = false;
    bool check = true;
    std::cout<<"Добро пожаловать в генератор никнеймов";
    while (check == true){
        int parameter;
        std::cout<<"1 - запустить генератор никнеймов; 2 - редактирование списков;  0 - выйти из программы\
        \nВведите параметр: ";
        std::cin>>parameter;
        switch (parameter){
            case 1:{
            int howmuch;
            std::cout<<"Введите желаемое количество никнеймов: ";
            std::cin>>howmuch;
            cout<<  
            if (isGenerated == false)
            {
                generator("","", massWord, massNames);
                isGenerated = true;
            }
            printNames(howmuch);
            // for ()
            // {

            // }
            break;
            }

        }
    }
    return 0;
}