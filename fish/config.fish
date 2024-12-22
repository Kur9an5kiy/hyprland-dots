if status is-interactive
	set fish_greeting
	abbr -a ys yay -S
	abbr -a yss yay -Ss
	abbr -a yr yay -R
	abbr -a yy yay -Sy
	abbr -a yyu yay -Syu
	abbr -a ps sudo pacman -S
	abbr -a pss pacman -Ss
	abbr -a pr sudo pacman -R
	abbr -a py sudo pacman -Sy
	abbr -a pyu sudo pacman -Syu

	abbr -a cfg cd ~/.config/
	abbr -a scr cd ~/.scripts
	abbr -a hcfg cd ~/.config/hypr

	abbr -a v nvim
	abbr -a pcl peaclock
	abbr -a mt cmatrix
	abbr -a ff fastfetch
	abbr -a c cat
	abbr -a rmd rm -rf 
end
