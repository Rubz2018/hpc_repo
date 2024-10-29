program estimate_pi
    implicit none
    integer :: n, count, j, seed_size
    real :: x, y, r, pi
    real(8) :: start_time, end_time, elapsed_time
    integer, dimension(:), allocatable :: seed

    ! Initialize parameters
    n = 10000000
    count = 0

    ! Set the random seed using an array of the appropriate size
    call random_seed(size=seed_size)      ! Get the required size of the seed array
    allocate(seed(seed_size))
    seed = 12345                          ! Initialize seed values with any chosen number
    call random_seed(put=seed)            ! Set the random seed

    ! Start the timer
    call cpu_time(start_time)

    ! Loop through n random points
    do j = 1, n
        call random_number(x)             ! Generate random x in [0, 1]
        call random_number(y)             ! Generate random y in [0, 1]
        x = 2.0 * x - 1.0                 ! Scale x to [-1, 1]
        y = 2.0 * y - 1.0                 ! Scale y to [-1, 1]
        r = x**2 + y**2

        if (r <= 1.0) then
            count = count + 1
        end if
    end do

    ! Estimate Pi
    pi = 4.0 * real(count) / real(n)

    ! End the timer
    call cpu_time(end_time)
    elapsed_time = end_time - start_time

    ! Print results
    print '(A, F10.5)', 'pi: ', pi
    print '(A, I10)', 'i: ', count
    print '(A, I10)', 'n: ', n
    print '(A, F10.5)', 'The elapsed time: ', elapsed_time

    ! Deallocate seed array
    deallocate(seed)

end program estimate_pi
